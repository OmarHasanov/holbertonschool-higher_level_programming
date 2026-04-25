def generate_invitations(template, attendees):
    # 🔹 Type yoxlaması
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # 🔹 Empty yoxlaması
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 🔹 Placeholder list
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # 🔹 Hər attendee üçün fayl yarat
    for i, attendee in enumerate(attendees, start=1):
        result = template

        for key in placeholders:
            value = attendee.get(key)

            # None və ya missing → "N/A"
            if value is None:
                value = "N/A"

            result = result.replace("{" + key + "}", str(value))

        filename = f"output_{i}.txt"

        try:
            with open(filename, "w") as file:
                file.write(result)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
