import open3d as o3d

if __name__ == "__main__":
    file_name = "speaker5.ply_1677243611687.82519531250000.ply"
    pcd = o3d.io.read_point_cloud(file_name)
    o3d.visualization.draw(pcd)
