from setuptools import find_packages, setup

package_name = 'computer_vision_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test'], 
                           include=[package_name, f"{package_name}.*"]),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pipi',
    maintainer_email='vincent.pu@outlook.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
