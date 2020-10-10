import os


class FileWriter:

    @staticmethod
    def write_to_file(output_folder, file_name, to_write, encoding='utf-8', binary_file=False):
        arg = {"mode": "wb"} if binary_file else {"mode": "w", "encoding": encoding}
        print(file_name)
        try:
            with open(os.path.join(output_folder, file_name), **arg) as outfile:
                 outfile.write(to_write)

        except Exception as e:
            print("An error occured when trying to write on file : {} \n Error : {}".format(file_name, e))
