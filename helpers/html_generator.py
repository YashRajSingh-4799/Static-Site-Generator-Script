def generate_html_content(activity_data):
    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    
    <title>Dynamically Generated Page</title>
</head>
<body>
     

    <section class="text-gray-900 body-font px-10 py-24">
        
        <div class="px-5 py-4 mx-auto flex items-center sm:flex-row flex-col">
    
    <p class="text-sm text-white-900 sm:ml-4 sm:pl-4 sm:py-2 sm:mt-0 mt-4"> {activity_data["key"]} </p>
    
    
    <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
     <p>
        {activity_data["price"]}
     </p>
     
    </span>
  </div>
  <div class="container mx-auto flex px-5  md:flex-row flex-col items-center">
    <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
      <h1 class="title-font  text-5xl mb-4 font-medium text-gray-900">{activity_data["activity"]} 
        
      </h1>
      <p class="mb-8 leading-relaxed font-bold">OUTDOOR AND SPORTING GOODS COMPANY.</p>
      <div class="flex justify-center">
        <button class="inline-flex text-white bg-orange-500 border-0 py-2 px-6 focus:outline-none hover:bg-orange-600 rounded text-lg my-5 font-bold">EXPLORE MORE  -----> </button>
      </div>
      <p class="mb-8 leading-relaxed">We have more special goods for you...</p>
    </div>
    <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
      <img class="object-cover object-center rounded" alt="hero" src="./hero.jpeg">
      
    </div>
  </div>
</section>


<!-- Footer -->
<footer class="text-white body-font bgray">
  <div class="container px-5 py-8 mx-auto flex items-center sm:flex-row flex-col">
    
    <p class="text-sm text-white-900 sm:ml-4 sm:pl-4  sm:py-2 sm:mt-0 mt-4">{activity_data["accessibility"]}</p>
    
    
    <span class="inline-flex sm:ml-auto sm:mt-0 mt-4 justify-center sm:justify-start">
        <p>{activity_data["type"]}</p>

    </span>
  </div>
</footer>
<!-- End Footer -->
</body>
</html>

'''
