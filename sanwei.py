import numpy as np
import pandas as pd
import plotly.graph_objects as go

node_list = pd.read_csv('附件1.csv', encoding='gbk')
node_x = np.array(node_list['X坐标（米）'])
node_y = np.array(node_list['Y坐标（米）'])
node_z = np.array(node_list['Z坐标（米）'])

actuator_list = pd.read_csv('附件2.csv', encoding='gbk')
actuator_x_up = np.array(actuator_list['基准态时上端点X坐标（米）'])
actuator_y_up = np.array(actuator_list['基准态时上端点Y坐标（米）'])
actuator_z_up = np.array(actuator_list['基准态时上端点Z坐标（米）'])

actuator_x_down = np.array(actuator_list['下端点X坐标（米）'])
actuator_y_down = np.array(actuator_list['下端点Y坐标（米）'])
actuator_z_down = np.array(actuator_list['下端点Z坐标（米）'])

# 设置节点颜色和形状
marker_color = 'red'  # 设置节点颜色
marker_symbol = 'square'  # 设置节点形状

# 创建散点图
fig = go.Figure()
fig.add_trace(go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='markers',
                           marker=dict(color=marker_color, symbol=marker_symbol)))

# 修改节点颜色和形状
marker_color = 'blue'
fig.add_trace(go.Scatter3d(x=actuator_x_up, y=actuator_y_up, z=actuator_z_up, mode='markers',
                           marker=dict(color=marker_color, symbol=marker_symbol)))

# 修改节点颜色和形状
marker_color = 'yellow'
fig.add_trace(go.Scatter3d(x=actuator_x_down, y=actuator_y_down, z=actuator_z_down, mode='markers',
                           marker=dict(color=marker_color, symbol=marker_symbol)))

# 设置初始视角
fig.update_layout(scene_camera=dict(eye=dict(x=1.5, y=1.5, z=0.8)))

# 显示图形
fig.show()
