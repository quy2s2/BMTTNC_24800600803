from PIL import Image
import os

def hide_message(image_path, message, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')
        # Get the pixel data
        pixels = list(img.getdata())
        
        # Convert message to binary
        binary = ''.join(format(ord(i), '08b') for i in message)
        
        # Make sure the image is big enough
        if len(binary) > len(pixels):
            raise ValueError("Message too large for image")
        
        # Create new pixel data with hidden message
        new_pixels = []
        binary_index = 0
        
        for i, pixel in enumerate(pixels):
            if binary_index < len(binary):
                # Get current RGB values
                r, g, b = pixel
                # Modify least significant bit of Red value to store message bit
                r = r & ~1 | int(binary[binary_index])
                new_pixels.append((r, g, b))
                binary_index += 1
            else:
                new_pixels.append(pixel)
        
        # Create new image with hidden message
        new_img = Image.new(img.mode, img.size)
        new_img.putdata(new_pixels)
        
        # Save the new image
        new_img.save(output_path, 'PNG')
        print(f"Successfully created encoded image at {output_path}")
        
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise e

if __name__ == '__main__':
    # Get the absolute path to the static directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir, 'static')
    
    # Define input and output paths
    input_path = os.path.join(static_dir, 'hutech_30.jpg')
    output_path = os.path.join(static_dir, 'hutech_30_encoded.png')
    
    print(f"Input path: {input_path}")
    print(f"Output path: {output_path}")
    
    # Hide the message in the image
    try:
        hide_message(input_path, 'HUTECH30NAM', output_path)
        print("Process completed successfully!")
    except Exception as e:
        print(f"Failed to create encoded image: {str(e)}")
