import os
import pygame
import shutil

# Set up directories
images_folder = "./"
dir_right = './Keep'
dir_left = './Skip'
screen_width = 800
screen_height= 600

def main():
    # Create directories if they don't exist
    os.makedirs(dir_right, exist_ok=True)
    os.makedirs(dir_left, exist_ok=True)

    # Load all images from the folder
    image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Initialize Pygame
    pygame.init()

    # Define screen size and create display surface
    screen = pygame.display.set_mode((screen_width, screen_height))  
    pygame.display.set_caption("Image Sorting")

    # Main loop to render images and listen for input
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)

        # Render the current image
        img = pygame.image.load(image_path)
        # Calculate center position
        image_width = img.get_width()
        image_height = img.get_height()
        x = (screen_width - image_width) // 2
        y = (screen_height - image_height) // 2

        screen.blit(img, (x, y))
        pygame.display.update()

        sorting = True
        while sorting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # Move to Directory A (left)
                    if event.key == pygame.K_LEFT:  
                        shutil.move(image_path, os.path.join(dir_left, image_file))
                        # Proceed to next image
                        sorting = False  
                    # Move to Directory B (right)
                    elif event.key == pygame.K_RIGHT:  
                        shutil.move(image_path, os.path.join(dir_right, image_file))
                        # Proceed to next image
                        sorting = False  

    pygame.quit()

if __name__ == '__main__':
    main()
