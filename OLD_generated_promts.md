# **Optimal Prompt for Automating Research Paper Comic Generation**

## **Task Overview**
"I want to convert a research paper into an easy-to-understand comic with minimal human intervention. Follow these steps precisely to extract key information, generate structured scenes, create AI-generated images, and compile a structured JSON file for dynamic rendering."

---

## **Step 1: Understanding & Structuring the Research Paper**
1. **Extract key insights** from the uploaded PDF:
   - Identify the **main problem** discussed in the research.
   - Summarize the **proposed solution** and any technical contributions.
   - Outline the **core findings** and future directions.

2. **Break the research paper into a comic-friendly format** with structured storytelling:
   - **Scene 1: Problem Introduction** (Why does this research matter?)
   - **Scene 2: Solution/Methodology** (How does it address the problem?)
   - **Scene 3: Challenges & Threat Models** (What are the risks or limitations?)
   - **Scene 4: Future Outlook & Impact** (Why is this important?)

---

## **Step 2: Character Generation & Consistency Handling**
1. **Generate 3-5 unique character names**, each with a **distinct role** (e.g., researcher, user, hacker, industry expert).
2. **Describe their personalities, appearances, and roles** to maintain consistency across all scenes.
3. **Ensure character consistency in AI-generated images** by using:
   - Fixed character names in text prompts.
   - A consistent descriptive format for character appearance.

---

## **Step 3: Scene Breakdown & Image Generation**
1. **For each scene, generate a structured description of 4 panels:**
   - **Panel 1:** The introductory visual.
   - **Panel 2:** Core research problem or method.
   - **Panel 3:** Experimental demonstration.
   - **Panel 4:** Summary or reaction of key characters.

2. Each **panel should include:**
   - **A prompt for image generation** (e.g., “A researcher presenting results on a futuristic holographic screen”).
   - **A dialogue/narration text** that matches the image.

3. **Generate comic-style images** using a text-to-image model (e.g., DALL·E) for each panel.
   - Ensure images have **consistent art style** (e.g., digital comic, cyberpunk, scientific).
   - Adjust **expressions & perspectives** dynamically to match storytelling.

---

## **Step 4: JSON Structuring for Automated Rendering**
1. **For each generated image, create a JSON entry structured as follows:**

   ```json
   {
       "scene_1": [
           {
               "image_id": "0",
               "text": "Narration: 'Eye-tracking in VR makes experiences more immersive... but what if it also tracks who you are?'",
               "description": "Lisa Kim wearing a VR headset in a high-tech lab, with her eye movements being tracked."
           },
           {
               "image_id": "1",
               "text": "Dr. Carter: 'Studies show that eye movements can be used to re-identify users with up to 85% accuracy!'",
               "description": "A computer screen displaying profiles being reconstructed from eye-tracking data."
           },
           {...}
       ],
       "scene_2": [...]
   }
   ```
2. **Ensure proper sorting and linking between images and dialogues using lexically ordered filenames (0.png, 1.png, …)**