import os
import sys
import argparse

import pkg_resources

def main():
    parser = argparse.ArgumentParser(description='Freeze Python package dependencies')
    parser.add_argument('source', help='requirements.txt formatted file with dependencies to freeze')
    parser.add_argument('dest', help='path to a new requirements.txt formatted file that will be written with frozen dependencies')
    args = parser.parse_args()

    source_file_path = os.path.realpath(args.source)
    if not os.path.exists(source_file_path):
        raise IOError('Source file not found: {}'.format(source_file_path))
    dest_file_path = os.path.realpath(args.dest)
    if os.path.exists(dest_file_path):
        raise IOError('Destination file already exists, refusing to overwrite: {}'.format(dest_file_path))

    with open(source_file_path, 'r') as f:
        source_lines = f.readlines()

    # construct the frozen requirements
    frozen_requirements = []
    for package_spec in filter(None, source_lines):
        try:
            package_name = pkg_resources.Requirement.parse(package_spec).project_name
        except ValueError as e:
            print 'Could not parse requirements, will copy it directly: {}'.format(package_spec.strip())
            if package_spec not in frozen_requirements:
                frozen_requirements.append(package_spec)
            continue

        try:
            subpackages = pkg_resources.require(package_name)
        except pkg_resources.DistributionNotFound as e:
            print 'Distribution not found for this spec, is it installed? : {}'.format(package_name)
            print 'Freeze aborting, frozen requirements were not saved.'
            sys.exit(1)

        for subpackage in subpackages:
            spec = '{}=={}'.format(subpackage.project_name, subpackage.version)
            if spec not in frozen_requirements:
                frozen_requirements.append(spec)

    # write the freeze file
    with open(dest_file_path, 'w') as f:
        for package_spec in frozen_requirements:
            f.write('{}\n'.format(package_spec.strip()))

    print 'Successfully froze requirements to {}'.format(dest_file_path)

if __name__ == '__main__':
    main()
