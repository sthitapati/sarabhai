from utils.preprocess_utils import *

def main():
    arguments = parse_arguments()
    metadata = ConfigParser(metadata_file=arguments['metadata'])
    metadata.parse_metadata()
    process_animal_data(animal_ids= metadata.animal_ids,
                        input_directory=metadata.input_directory,
                        output_directory=metadata.output_directory,
                        camera_directory=metadata.camera_directory,
                        replace_existing=arguments['replace']
                        )


if __name__ == "__main__":
    main()