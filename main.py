import requests
import os
from helpers.html_generator import generate_html_content

# Function to fetch activity data from the API
def fetch_activity_data():
    response = requests.get('https://www.boredapi.com/api/activity')
    return response.json()

# Function to write the generated HTML to a file
def write_html_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

# Main function to generate and deploy pages
def generate_and_deploy_pages(num_pages):
    # Create a folder to store the generated pages
    if not os.path.exists('generated_pages'):
        os.makedirs('generated_pages')

    for i in range(num_pages):
        # Fetch activity data from the API
        activity_data = fetch_activity_data()

        # Generate HTML content with the activity data
        html_content = generate_html_content(activity_data)

        # Write the HTML content to a file
        filename = f'generated_pages/page_{i + 1}.html'
        write_html_file(html_content, filename)

    # Deploy the generated pages to Vercel using the vercel-cli
    os.chdir('generated_pages')
    os.system('vercel --prod')
    os.chdir('..')

if __name__ == "__main__":
    num_pages = int(input("Enter the number of pages to generate: "))
    generate_and_deploy_pages(num_pages)
