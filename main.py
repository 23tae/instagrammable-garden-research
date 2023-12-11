import time
import input_data
import directory
import analyzer

image_root_dir = '../instagram-image-downloader/result/'
methods = ['labels', 'properties']


def main():
    start = time.time()
    profiles = input_data.get_profiles(image_root_dir)
    directory.make_output_directory(profiles, methods)
    analyzer.analyze_images(profiles, image_root_dir, methods)
    elapsed_time = time.time() - start
    elapsed_time_rounded = round(elapsed_time, 2)
    print("Total time:", str(elapsed_time_rounded) + 's')


if __name__ == '__main__':
    main()
