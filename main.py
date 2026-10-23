import cv2
from ring_service import RingAccessController

def main():
    print("TruePresence - Offline Face Verification Started")
    print("Hardware: Any 720p cam | Mode: 100% Offline | Speed: <1 sec")
    
    controller = RingAccessController()
    
    # For hackathon: Using webcam as Ring Camera Simulator
    # Real dlib code will be here - placeholder for demo
    cap = cv2.VideoCapture(0)
    print("Press 'q' to verify, 'Esc' to exit")
    
    # Simulate verification
    controller.verify_and_unlock("komalsaha8")
    
    cap.release()

if __name__ == "__main__":
    main()
