using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace calling_card.Controllers
{
    public class CardsController : Controller
    {

        [HttpGet]
        [Route("/{FirstName}/{LastName}/{Age}/{FavColor}")]
        public JsonResult CallCard(string FirstName, string LastName, int Age, string FavColor)
        {
            //This builds a JSON response with the given route parameters
            return Json(new {FirstName = FirstName, LastName = LastName, Age = Age, FavoriteColor = FavColor});
        }
    }
}

