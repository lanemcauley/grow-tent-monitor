import cv2
import os

def create_mp4_from_jpgs(image_folder, output_video_path, fps=24):
        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
        images.sort() # Ensure images are in correct order for video sequence

        if not images:
            print("No JPG images found in the specified folder.")
            return

        # Read the first image to get dimensions
        first_image_path = os.path.join(image_folder, images[0])
        frame = cv2.imread(first_image_path)
        height, width, layers = frame.shape

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'avc1') 
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

        for image_name in images:
            image_path = os.path.join(image_folder, image_name)
            frame = cv2.imread(image_path)
            out.write(frame)

        out.release()
        print(f"mp4 video created at: {output_video_path}")

    # Example usage:
#create_mp4_from_jpgs("/home/lane/grow-tent-monitor/static/snapshots", "/home/lane/grow-tent-monitor/static/current_timelapse.mp4", fps=5)