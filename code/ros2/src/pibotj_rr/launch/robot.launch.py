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
            package='pibotj_rr',
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
            package='pibotj_rr',
            executable='motors_controller_web_node',
            name='motors_controller_web_node',
            output='screen'
        ),

        # Ejecutar camera_tfv2_node funciona
        #Node(
        #    package='pibotj_rr',
        #    executable='camera_tfv2_node',
        #    name='camera_tfv2_node',
        #    output='screen'
        #),

        #ExecuteProcess(
        #    cmd=['bash', '-c', "renice -n -10 $(pgrep -f 'camera_tfv2_node')"],
        #    shell=True,
        #    output='screen'
        #),

        #TimerAction(
        #    period=10.0,
        #    actions=[
        #        ExecuteProcess(
        #            cmd=['bash', '-c', "renice -n -10 $(pgrep -f 'camera_tfv2_node')"],
        #            shell=True,
        #            output='screen'
        #        )
        #    ]
        #)

        #ExecuteProcess(
        #    cmd=['sudo','nice', '-n', '-10', 'ros2', 'run', 'pibotj_rr', 'camera_tfv2_node'],
        #    output='screen'
        #),
    ])
