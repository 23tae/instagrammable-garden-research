import os


def make_output_directory(profiles: dict, methods: list):
    for category, names in profiles.items():
        for method in methods:
            out_dir = os.path.join(os.getcwd(), 'result', category, method)
            os.path.exists(out_dir) or os.makedirs(out_dir)
            for name in names:
                out_dir = os.path.join(
                    os.getcwd(), 'result', category, method, name)
                os.path.exists(out_dir) or os.makedirs(out_dir)
