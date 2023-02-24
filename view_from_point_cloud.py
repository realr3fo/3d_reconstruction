import open3d as o3d

if __name__ == "__main__":
    file_name = "speaker2.ply_1677242216965.86499023437500.ply"
    pcd = o3d.io.read_point_cloud(file_name)
    o3d.visualization.draw(pcd)
