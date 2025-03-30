# **Optimal Prompt for Automating Research Paper Comic Generation**

## **Task Overview**
"I want to convert a research paper into an easy-to-understand comic with minimal human intervention. The process should dynamically adjust based on the paper’s complexity and technical depth. The system must ensure dialogue and structure are confirmed before generating images. Follow these steps precisely to extract key information, generate structured scenes, confirm dialogues, and create AI-generated images."

---

## **Step 1: Understanding & Structuring the Research Paper**
1. **Extract key insights** from the uploaded PDF:
   - Identify the **main problem** discussed in the research.
   - Summarize the **proposed solution** and any technical contributions.
   - Outline the **core findings** and future directions.

2. **Adapt the comic structure dynamically** based on technical depth:
   - **If highly technical**, expand the methodology section across multiple scenes.
   - **If broad in implications**, combine challenges and future outlook into one scene.

3. **Structure the comic into distinct storytelling scenes** based on extracted content:
   - **Scene 1: Problem Introduction** (Why does this research matter?)
   - **Scene 2: Solution/Methodology** (How does it address the problem?)
   - **Scene 3: Demonstration & Results** (What does the research prove?)
   - **Scene 4: Implications & Future Impact** (What are the risks, challenges, and future use cases?)
   - **(Adjust scene structure as needed to fit the research content)**

---

## **Step 2: Character Generation & Consistency Handling**
1. **Define 3-5 unique characters** with distinct roles (e.g., researcher, journalist, hacker, AI assistant).
2. **Describe personalities, appearances, and roles** to maintain consistency across all scenes.
3. **Confirm character consistency in AI-generated images** by using:
   - Fixed character names in text prompts.
   - A structured format for appearance descriptions.

---

## **Step 3: Scene Breakdown & Dialogue Confirmation**
1. **For each scene, generate a structured breakdown** with 4 panels per scene:
   - **Panel 1:** Introduction or setup.
   - **Panel 2:** Explanation of the core problem or method.
   - **Panel 3:** Demonstration or evidence.
   - **Panel 4:** Reaction or summary by key characters.

2. **Before generating images, confirm dialogue and descriptions** with the user:
   - Present a structured draft with character dialogues and scene descriptions.
   - Allow adjustments before finalizing prompts.

---

## **Step 4: AI Image Generation & Rendering Adjustments**
1. **Generate AI-powered comic images** for each panel:
   - Use a consistent **art style** (e.g., digital comic, sci-fi research lab, cyberpunk, etc.).
   - Ensure **character expressions and poses** match the dialogue.

2. **Maintain scene flow and layout consistency** by:
   - Keeping **characters' appearances consistent** across different panels.
   - Adjusting **perspectives and expressions dynamically** to match storytelling.

---

## **Step 5: JSON Structuring for Automated Rendering**
1. **Create a structured JSON file** for dynamic rendering of the comic:

   ```json
   {
       "scene_1": [
           {
               "image_id": "0",
               "text": "Lisa: 'This face swap looks impressive, but something feels… off.'",
               "description": "Dr. Wilson showing Lisa a face swap demo in a high-tech lab."
           },
           {
               "image_id": "1",
               "text": "Dr. Wilson: 'Face swap models struggle with gaze misalignment!'",
               "description": "A side-by-side comparison of a deepfake with incorrect vs. correct gaze alignment."
           }
       ],
       "scene_2": [...]
   }
