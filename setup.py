from setuptools import setup

package_name = 'sofar_assignment'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/'+package_name]))
data_files.append(('share/'+package_name+'/launch', ['launch/robot_launch.py']))
data_files.append(('share/'+package_name+'/worlds', ['worlds/default.wbt']))
data_files.append(('share/'+package_name+'/resource', [
	'resource/tiago_webots.urdf',
	'resource/default.rviz',
	'resource/map.pgm',
	'resource/map.yaml',
	'resource/ros2_control.yml'
	]))
data_files.append(('share/'+package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='davide',
    maintainer_email='davide.parisi1084@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
