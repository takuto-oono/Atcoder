import os

test_file = 'test_test.py'

n = 4

def create_file_name(name, index):
    return name + str(index + 1) + '.txt'

def run():
    for i in range(n):
        input_file = create_file_name('input', i)
        output_file = create_file_name('output', i)
        command = 'python3 ' + test_file
        os.system("python3 " + test_file + ' < ' + input_file + ' > ' + output_file)
    

def read_file(file_name):
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def judge():
    for i in range(n):
        output_file = create_file_name('output', i)
        ans_file = create_file_name('ans', i)
        
        output_data = read_file(output_file)
        ans_data = read_file(ans_file)
        
        if output_data == ans_data:
            print('test case' + str(i + 1) + ' True')
        else:
            print('test case' + str(i + 1) + ' False')

if __name__ == '__main__':
    run()
    judge()
    