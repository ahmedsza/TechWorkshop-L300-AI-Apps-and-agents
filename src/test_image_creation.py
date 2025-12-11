import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.tools.imageCreationTool import create_image

# Load environment variables
load_dotenv()

def test_image_creation():
    """Test the image creation/edit tool directly"""
    
    # Test with the local living room image
    image_path = os.path.join(os.path.dirname(__file__), "data", "LivingRoomImage.jpg")
    
    print(f"Testing image creation tool...")
    print(f"Image path: {image_path}")
    print(f"Checking if image exists: {os.path.exists(image_path)}")
    
    if not os.path.exists(image_path):
        print(f"ERROR: Image file not found at {image_path}")
        return
    
    # Test prompt - repaint walls in Pale Meadow color
    prompt = "Repaint the walls in pink"
    
    print(f"\nPrompt: {prompt}")
    print("\nCalling create_image function...")
    
    try:
        result_url = create_image(prompt, image_path)
        
        if result_url:
            print(f"\n✓ SUCCESS!")
            print(f"Generated image URL: {result_url}")
        else:
            print("\n✗ FAILED: No URL returned")
            
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Check environment variables
    print("Checking environment variables...")
    required_vars = ["gpt-image-1-endpoint", "gpt-image-1-deployment", "gpt-image-1-api_version", "subscription_key"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"WARNING: Missing environment variables: {', '.join(missing_vars)}")
    else:
        print("✓ All required environment variables are set")
    
    print("\n" + "="*60)
    test_image_creation()
    print("="*60)
