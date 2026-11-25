from setuptools import find_packages, setup

package_name = 'kinova_gen3_teleop'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Uzayr Rafiq',
    maintainer_email='u.rafiq2005@gmail.com',
    description='Keyboard control for a simulated Kinova Gen3 arm.',
    license='TODO',
    entry_points={
        'console_scripts': [
            'keyboard_node = kinova_gen3_teleop.keyboard_node:main',
        ],
    },
)
