class Logger:

    @staticmethod
    def write_into_file(list_, file_name='Result.txt'):
        f = open(file_name, 'a')
        f.write(str(list_) + '\n')
        f.close()
