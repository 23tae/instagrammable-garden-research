import sys
import os
import input_data
import directory
import detect

# image_root_dir = '../instagram-image-downloader/result/'
image_root_dir = '../instagram-image-downloader/test/'
methods = ['labels', 'properties', 'object-localization']


def analyze_images(profiles):
    output_root_dir = os.path.join(os.getcwd(), 'result')
    for category, names in profiles.items():  # per category
        for name in names:  # per user
            for i in range(50):  # per image
                if os.path.exists(os.path.join(image_root_dir, category, name, str(i) + '.jpg')):
                    for method in methods:
                        sys.stdout = open(os.path.join(
                            output_root_dir, category, method, name, str(i) + '.txt'), 'w')
                        if method == 'labels':
                            detect.detect_labels(os.path.join(
                                image_root_dir, category, name, str(i) + '.jpg'))
                        elif method == 'properties':
                            detect.detect_properties(os.path.join(
                                image_root_dir, category, name, str(i) + '.jpg'))
                        elif method == 'object-localization':
                            detect.localize_objects(os.path.join(
                                image_root_dir, category, name, str(i) + '.jpg'))
                        else:
                            print('invalid method')
                        sys.stdout.close()
                else:  # no image
                    break


def main():
    profiles = input_data.get_profiles(image_root_dir)
    directory.make_output_directory(profiles, methods)
    analyze_images(profiles)


if __name__ == '__main__':
    main()
