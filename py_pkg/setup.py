from setuptools import find_packages, setup

package_name = 'py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ceejay',
    maintainer_email='0xceejay@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "minimal_publisher = py_pkg.minimal_publisher:main",
            "minimal_subscriber = py_pkg.minimal_subscriber:main",
            "minimal_server = py_pkg.minimal_server:main",
            "minimal_client = py_pkg.minimal_client:main",
            "acc_publisher = py_pkg.acc_publisher:main",
            "trigger_points_server = py_pkg.trigger_points_server:main",
        ],
    },
)
