import os
import gradio as gr
import joblib

# Load the trained model
deployed_lr = joblib.load("my_first_ml_model.pkl")


def predict_rent(bhk, size_of_prop):
    prediction = deployed_lr.predict([[bhk, size_of_prop]])
    return f"Estimated Rent: ${prediction[0]:.2f}"


custom_css = """
.gradio-container {
    background-image: url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.glass-container {
    background-color: rgba(255,255,255,0.95) !important;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
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

with gr.Blocks(css=custom_css, title="Property Rent Predictor") as interface:

    with gr.Column(elem_classes="glass-container"):

        gr.Markdown("<h1 style='text-align:center;'>🏙️ Property Rent Predictor</h1>")
        gr.Markdown("<p style='text-align:center;'>Enter the property details to estimate rent.</p>")

        gr.HTML("<hr>")

        with gr.Row():

            # Left Side
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

            # Right Side
            with gr.Column(scale=1):

                gr.Markdown("### 👨‍💻 About the Developer")
                gr.Markdown("**Nandini Goel**")

                gr.Markdown("### 🛠️ Tools Used")
                gr.Markdown("""
- **Python**
- **Gradio**
- **Scikit-Learn**
- **Joblib**
""")

if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
