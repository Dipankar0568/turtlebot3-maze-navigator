from setuptools import setup

package_name = 'turtlebot3_navigator'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
	('share/' + package_name + '/launch', ['launch/lidar_avoidance.launch.py']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dipankar',
    maintainer_email='bagadedrm222@gmail.com',
    description='TurtleBot3 Obstacle Avoidance Node using LIDAR',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_avoidance = turtlebot3_navigator.lidar_avoidance:main',
        ],
    },
)
