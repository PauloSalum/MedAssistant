# MedAssistant

MedAssistant is a custom integration for Home Assistant designed to help users manage and track their medication intake. With MedAssistant, you can register your medications, set daily doses, consumption times, and receive notifications when it's time to take your medicine. It also alerts you when your medication supply is running low.

## Features

- Register medications with details such as name, box quantity, number of boxes in possession, daily dose, and consumption times.
- Daily tracking of medication intake with notifications for dose times.
- Confirmation system for taken doses, automatically updating remaining doses.
- Advance notifications when medication supplies are running low (one week in advance).

## Installation

1. **Clone this repository** to your local machine or download the ZIP file.
2. **Copy the `medassistant` folder** to the `custom_components` directory of your Home Assistant installation.
3. **Restart Home Assistant** to recognize the new integration.

## Configuration

After installation, you need to configure MedAssistant via the Home Assistant UI.

1. Go to **Settings** > **Devices & Services** > **Integrations**.
2. Click on the **Add Integration** button and search for `MedAssistant`.
3. Follow the on-screen instructions to configure your medications.

## Usage

Once configured, MedAssistant will start tracking your medication schedules. You will receive notifications based on the times you've set for each medication. You can confirm medication intake directly from the notification, and MedAssistant will update the remaining doses accordingly.

## Notifications

- **Dose Reminder:** You'll receive a reminder when it's time to take a specific medication.
- **Low Supply Alert:** When a medication's supply drops below a week's worth of doses, you'll get an alert to restock.

## Contributing

Contributions to MedAssistant are welcome! If you have suggestions for improvements or bug fixes, please open an issue or submit a pull request.

## License

MedAssistant is released under the [MIT License](LICENSE).
