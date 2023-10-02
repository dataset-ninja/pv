import supervisely as sly
import os, glob
from dataset_tools.convert import unpack_if_archive
import src.settings as s
from urllib.parse import unquote, urlparse
from supervisely.io.fs import get_file_name, get_file_name_with_ext
import shutil

from tqdm import tqdm

def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:        
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path
    
def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count
    
def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/home/alex/DATASETS/TODO/photovoltaic panel segmentation/archive"
    ds_name = "ds"
    batch_size = 30
    masks_suffix = "_label.bmp"


    def create_ann(image_path):
        labels = []

        tag_value = image_path.split("/")[-3]
        tag_meta = meta.get_tag_meta(tag_value)
        tag = sly.Tag(tag_meta)

        category_value = image_path.split("/")[-2][5:]
        category = sly.Tag(tag_category, value=category_value)

        image_name = get_file_name(image_path)
        mask_path = os.path.join(
            dataset_path, tag_value, image_path.split("/")[-2], image_name + masks_suffix
        )
        mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
        img_height = mask_np.shape[0]
        img_wight = mask_np.shape[1]
        mask = mask_np != 0
        # ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
        # for i in range(1, ret):
        #     obj_mask = curr_mask == i
        curr_bitmap = sly.Bitmap(mask)
            # if curr_bitmap.area >= 10:
        curr_label = sly.Label(curr_bitmap, obj_class)
        labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[tag, category])


    obj_class = sly.ObjClass("photovoltaic panel", sly.Bitmap)

    tag_pv01 = sly.TagMeta("PV01", sly.TagValueType.NONE)
    tag_pv03 = sly.TagMeta("PV03", sly.TagValueType.NONE)
    tag_pv08 = sly.TagMeta("PV08", sly.TagValueType.NONE)
    tag_category = sly.TagMeta("category", sly.TagValueType.ANY_STRING)


    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class], tag_metas=[tag_pv01, tag_pv03, tag_pv08, tag_category]
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)


    all_images_pathes = glob.glob(dataset_path + "/*/*/*.bmp")
    images_pathes = [
        im_path for im_path in all_images_pathes if len(get_file_name(im_path).split("_")) != 4
    ]

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

    for images_pathes_batch in sly.batched(images_pathes, batch_size=batch_size):
        img_names_batch = [get_file_name_with_ext(img_path) for img_path in images_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))

    return project
