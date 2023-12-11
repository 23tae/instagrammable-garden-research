import sys
import os
import input_data
import directory
import detect
import time

image_root_dir = '../instagram-image-downloader/result/'
methods = ['labels', 'properties', 'object-localization']


def analyze_images(profiles):
    print('Analyzing images...\n')
    output_root_dir = os.path.join(os.getcwd(), 'result')
    for category, names in profiles.items():  # per category
        print('category:', category)
        for name in names:  # per user
            print('user:', name)
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
                        sys.stdout = sys.__stdout__

                else:  # no image
                    break
    print('Done.\n')


def main():
    start = time.time()
    profiles = input_data.get_profiles(image_root_dir)
    directory.make_output_directory(profiles, methods)
    analyze_images(profiles)
    elapsed_time = time.time() - start
    elapsed_time_rounded = round(elapsed_time, 2)
    print("Total time:", str(elapsed_time_rounded) + 's')


if __name__ == '__main__':
    main()
