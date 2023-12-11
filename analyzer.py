import sys
import os
import detect

image_number = 20


def analyze_images(profiles, image_root_dir, methods):
    print('Analyzing images...\n')
    output_root_dir = os.path.join(os.getcwd(), 'result')
    for category, names in profiles.items():  # per category
        print('category:', category)
        for name in names:  # per user
            print('user:', name)
            for i in range(image_number):  # per image
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
