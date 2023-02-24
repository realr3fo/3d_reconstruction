import open3d as o3d

dev = o3d.t.io.RealSenseSensor.list_devices()
print(dev)
