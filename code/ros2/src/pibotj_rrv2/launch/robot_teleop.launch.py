from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.actions import TimerAction

def generate_launch_description():
    return LaunchDescription([
        # Ejecutar rosbridge_server
        ExecuteProcess(
            cmd=['ros2', 'launch', 'rosbridge_server', 'rosbridge_websocket_launch.xml'],
            output='screen'
        ),

        # Ejecutar gps_node
        Node(
            package='pibotj_rrv2',
            executable='gps_node',
            name='gps_node',
            output='screen'
        ),

        # Ejecutar servidor HTTP en puerto 8000
        ExecuteProcess(
            cmd=['python3', '-m', 'http.server', '8000'],
            output='screen'
        ),

        # Ejecutar motors_controller_web_node
        Node(
            package='pibotj_rrv2',
            executable='motors_controller_web_node',
            name='motors_controller_web_node',
            output='screen'
        ),

        # Ejecutar camera_tfv3_node 
        Node(
            package='pibotj_rrv2',
            executable='camera_tfv3_node',
            name='camera_tfv3_node',
            output='screen'
        ),

        # Ejecutar camera_pinhole_web_node
        Node(
            package='pibotj_rrv2',
            executable='camera_pinhole_web_node',
            name='camera_pinhole_web_node',
            output='screen'
        )
    ])
