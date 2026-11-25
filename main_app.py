import customtkinter as ctk
from tkinter import filedialog

# Set the overall theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class CanLocalizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("FRC CAN Localizer")
        self.geometry("800x600")
        self.minsize(800, 600)

        # Create a tabview (like tabs in a browser)
        self.tabview = ctk.CTkTabview(self, width=750, height=550)
        self.tabview.pack(padx=20, pady=20, expand=True)
        
        self.tabview.add("Diagnosis")
        self.tabview.add("Settings")

        self.build_diagnosis_tab()
        self.build_settings_tab()

    def build_diagnosis_tab(self):
        tab = self.tabview.tab("Diagnosis")
        
        # Title
        title = ctk.CTkLabel(tab, text="CAN Bus Diagnostics", font=("Arial", 24, "bold"))
        title.pack(pady=(20, 10))

        # Upload Button
        self.upload_btn = ctk.CTkButton(tab, text="Upload Schematic Image", command=self.upload_schematic)
        self.upload_btn.pack(pady=10)

        # Status text
        self.status_label = ctk.CTkLabel(tab, text="No schematic loaded.", text_color="gray")
        self.status_label.pack(pady=5)

        # Run Diagnosis Button
        self.run_btn = ctk.CTkButton(tab, text="Run Diagnosis", fg_color="green", hover_color="darkgreen", height=40)
        self.run_btn.pack(pady=30)
        
        # Output Box
        self.output_box = ctk.CTkTextbox(tab, width=600, height=200, font=("Consolas", 14))
        self.output_box.pack(pady=10)
        self.output_box.insert("0.0", "Diagnostic results will appear here...\n")
        self.output_box.configure(state="disabled") # Make it read-only

    def build_settings_tab(self):
        tab = self.tabview.tab("Settings")
        
        title = ctk.CTkLabel(tab, text="API Configuration", font=("Arial", 20, "bold"))
        title.pack(pady=(20, 10))

        info_label = ctk.CTkLabel(tab, text="Paste your API key below.", wraplength=500)
        info_label.pack(pady=10)

        # API Key Input
        self.api_entry = ctk.CTkEntry(tab, width=400, placeholder_text="AIzaSy...", show="*")
        self.api_entry.pack(pady=10)

        # Save Button
        self.save_key_btn = ctk.CTkButton(tab, text="Save Key Securely", command=self.save_key)
        self.save_key_btn.pack(pady=10)

    def upload_schematic(self):
        filepath = filedialog.askopenfilename(
            title="Select Schematic",
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if filepath:
            self.status_label.configure(text=f"Loaded: {filepath}", text_color="white")
            self.current_image_path = filepath

    def save_key(self):
        # We will connect this to BYOK_FRC_CAN.py later!
        key = self.api_entry.get()
        if key:
            print(f"Saving key: {key}") # Placeholder for now
            self.api_entry.delete(0, 'end')
            self.api_entry.configure(placeholder_text="Key saved successfully!")

if __name__ == "__main__":
    app = CanLocalizerApp()
    app.mainloop()