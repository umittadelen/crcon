import os, shutil

package_directory = "package"
os.chdir(package_directory)

while True:
    answer = input(
'''1: install library
2: uninstall library
3: build
4: upload to pypi.org
5: install from file
> ''')

    if answer == '1':
        os.system("pip install crcon -U")
    elif answer == '2':
        os.system("pip uninstall crcon")
    elif answer == '3':
        if os.path.isdir('dist'):
            shutil.rmtree('dist')
        os.system("py -m build")
    elif answer == '4':
        os.system("py -m twine upload --repository pypi dist/*")
        os.system("py -m twine upload --repository testpypi dist/*")
    elif answer == '5':
        os.system("pip install .")
    else:
        print("Invalid choice. Please select a valid option.")
