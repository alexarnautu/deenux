
"""
Tool used to generate boilerplate
"""

import os

hm_path = os.path.realpath(os.path.dirname(__file__)) + '/'


def print_help():
    print("Help not implemented!")


def create_component(*args):
    if len(args) == 0:
        print("Please specify name of the component")
        return

    components_path = hm_path + '/../src/components'
    for name in args:

        comp_path = components_path + '/' + name.lower() + '/'
        if os.path.exists(comp_path):
            print ("A directory with the name `{0}` already exists".format(name))
            continue
        os.makedirs(comp_path)

        # Writing the view file
        with open(comp_path + name.capitalize() + '.py', 'w') as view:
            with open(hm_path + 'view_template') as view_template:
                view.write(view_template.read().format(name.lower(), name.capitalize()))

        # Writing the controller file
        with open(comp_path + name.capitalize() + 'Controller.py', 'w') as controller:
            with open(hm_path + 'controller_template') as controller_template:
                controller.write(controller_template.read().format(name.capitalize()))

        # Writing the init file
        with open(comp_path + '__init__.py', 'w'):
            pass



if __name__ == '__main__':
    import sys

    try:
        command = sys.argv[1]
        arg = sys.argv[2]
        args = sys.argv[3:]
        locals()[command + '_' + arg](*args)

    except:
        print_help()

