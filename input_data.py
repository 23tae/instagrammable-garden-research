import os


def get_profiles(image_root_dir: str):
    profiles = {}
    expanded_image_root_dir = os.path.expanduser(image_root_dir)
    category_dirs = os.listdir(expanded_image_root_dir)
    for category in category_dirs:  # category
        if category.startswith('.'):  # hidden file
            continue
        user_dirs = [d for d in os.listdir(
            expanded_image_root_dir + category) if not d.endswith('.DS_Store')]

        profiles[category] = user_dirs
    return profiles
