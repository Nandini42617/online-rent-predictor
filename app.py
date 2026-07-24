# app.py

import os 
#file handling
import gradio as gr
import joblib

# We load the model once when the app starts
deployed_lr = joblib.load('my_first_ml_model.pkl')

def predict_rent(bhk, size_of_prop):
    prediction = deployed_lr.predict([[bhk, size_of_prop]])
    return f"Estimated Rent: ${prediction[0]:.2f}"

# --- CODE BLOCK: UPDATED CSS FOR TEXT VISIBILITY ---
# Added explicit dark color overrides for text, headers, and links so they contrast against the white glass container
custom_css = """
.gradio-container {
    background-image: url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop'); 
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
.glass-container {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    color: #1f2937 !important; 
}
.glass-container h1, 
.glass-container h3, 
.glass-container p, 
.glass-container a, 
.glass-container ul, 
.glass-container li,
.glass-container strong {
    color: #1f2937 !important;
}
.glass-container a {
    color: #2563eb !important; 
    text-decoration: none;
}
.glass-container a:hover {
    text-decoration: underline;
}
"""
# ---------------------------------------------------

with gr.Blocks(css=custom_css, title="Property Rent Predictor") as interface:
    with gr.Column(elem_classes="glass-container"):
        gr.Markdown("<h1 style='text-align: center;'>🏙️ Property Rent Predictor</h1>")
        gr.Markdown("<p style='text-align: center;'>Enter the property size to get a rent estimate powered by Machine Learning.</p>")
        
        gr.HTML("<hr style='border-color: #d1d5db;'>")
        
        with gr.Row():
            # Left Column: The Predictor Tool
            with gr.Column(scale=2):
    gr.Markdown("### 📊 Estimation Tool")

    bhk_input = gr.Number(label="Enter Number of BHK")
    size_input = gr.Number(label="Please Enter the Size of Your Property for rent (sq ft)")

    predict_btn = gr.Button("Predict Rent", variant="primary")
    rent_output = gr.Text(label="Predicted Rent")

    predict_btn.click(
        fn=predict_rent,
        inputs=[bhk_input, size_input],
        outputs=rent_output
    )
    

    
    

    
    

    predict_btn.click(
        fn=predict_rent,
        inputs=[bhk_input, size_input],
        outputs=rent_output
    )
                
            
            # Right Column: Developer Details & Tools
            with gr.Column(scale=1):
                gr.Markdown("### 👨‍💻 About the Developer")
                gr.Markdown("**Nandini Goel**")
                
                
                gr.Markdown("### 🛠️ Tools Used")
                gr.Markdown("""
                * **Python**: Core programming language.
                * **Gradio**: Interactive web interface framework.
                * **Scikit-Learn**: Machine learning model training.
                * **Joblib**: Model serialization and loading.
                """)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
