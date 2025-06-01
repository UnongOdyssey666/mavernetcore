import os
import google.generativeai as genai

# Pastikan API Key Anda sudah di Replit Secrets dengan nama GEMINI_API_KEY
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not found in Replit Secrets.")
else:
    genai.configure(api_key=api_key)
    print("--- Listing available Gemini models ---")
    try:
        for m in genai.list_models():
            # Hanya tampilkan model yang mendukung generateContent (untuk percakapan)
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
        print("--- End of list ---")
        
        # Test the new model
        print("\n--- Testing gemini-1.5-flash model ---")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello, this is a test message.")
        print(f"✅ Model test successful: {response.text[:50]}...")
        
    except Exception as e:
        print(f"Error: {e}")
