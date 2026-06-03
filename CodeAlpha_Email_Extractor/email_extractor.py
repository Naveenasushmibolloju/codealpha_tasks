import re
import os

def extract_emails(input_file, output_file):
    """
    Extract email addresses from a text file
    and save them into another file.
    """

    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Find all email addresses
        emails = re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            content
        )

        # Remove duplicates and sort
        unique_emails = sorted(set(emails))

        with open(output_file, "w", encoding="utf-8") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print("=" * 60)
        print("           EMAIL ADDRESS EXTRACTOR")
        print("=" * 60)

        print(f"\nInput File          : {input_file}")
        print(f"Output File         : {output_file}")
        print(f"Total Emails Found  : {len(emails)}")
        print(f"Unique Emails Found : {len(unique_emails)}")

        print("\nExtracted Email Addresses:")
        print("-" * 60)

        for count, email in enumerate(unique_emails, start=1):
            print(f"{count}. {email}")

        print("\nEmail extraction completed successfully.")
        print(f"Results saved to '{output_file}'")

    except Exception as error:
        print(f"An error occurred: {error}")


# Main Program
print("=" * 60)
print("WELCOME TO EMAIL ADDRESS EXTRACTOR")
print("=" * 60)

input_filename = "input.txt"
output_filename = "extracted_emails.txt"

extract_emails(input_filename, output_filename)