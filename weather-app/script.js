async function getWeather() {
  const city = document.getElementById("cityInput").value;
  const resultDiv = document.getElementById("result");

  const apiKey = "2e209c272cd27724bfd3db7790f15765"; 

  try {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=ru`
    );

    if (!response.ok) {
      throw new Error("City not found. Please check the city name and try again.");
    }

    const data = await response.json();

    const temp = data.main.temp;
    const description = data.weather[0].description;

    resultDiv.innerHTML = `
      <p>Temperature: ${temp}°C</p>
      <p>Description: ${description}</p>
    `;
  } catch (error) {
    resultDiv.innerHTML = `<p style="color:red;">${error.message}</p>`;
  }
}