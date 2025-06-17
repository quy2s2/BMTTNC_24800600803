from PIL import Image
import numpy as np

def encode_message(img_path, message, output_path):
    # Load the image
    img = Image.open(img_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Convert message to binary
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    binary_message += '00000000'  # Add delimiter
    
    # Flatten the image array
    flat_img = img_array.flatten()
    
    # Encode message
    for i in range(len(binary_message)):
        if binary_message[i] == '1':
            flat_img[i] = flat_img[i] | 1
        else:
            flat_img[i] = flat_img[i] & ~1
    
    # Reshape array back to image dimensions
    encoded_img_array = flat_img.reshape(img_array.shape)
    
    # Create and save encoded image
    encoded_img = Image.fromarray(encoded_img_array)
    encoded_img.save(output_path, 'PNG')

def decode_message(img_path):
    # Load the encoded image
    img = Image.open(img_path)
    img_array = np.array(img)
    
    # Flatten the image array
    flat_img = img_array.flatten()
    
    # Extract binary message
    binary_message = ''
    for i in range(len(flat_img)):
        binary_message += str(flat_img[i] & 1)
        if len(binary_message) % 8 == 0:
            # Check for delimiter
            if binary_message[-8:] == '00000000':
                break
    
    # Convert binary to string
    message = ''
    for i in range(0, len(binary_message)-8, 8):
        message += chr(int(binary_message[i:i+8], 2))
    
    return message

if __name__ == "__main__":
    # Encode the message
    encode_message("hutech_30.jpg", "HUTECH30NAM", "hutech_30_encoded.png")
    
    # Verify the encoding
    decoded_message = decode_message("hutech_30_encoded.png")
    print(f"Decoded message: {decoded_message}")
