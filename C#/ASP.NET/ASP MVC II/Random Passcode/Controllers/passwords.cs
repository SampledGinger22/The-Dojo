using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
namespace Random_Passcode.Controllers;

public class HomeController : Controller 
{
    [HttpGet("")]
    
    public IActionResult passwordgen() 
    {
        if(HttpContext.Session.GetInt32("Visit") == null){
            HttpContext.Session.SetInt32("Visit", 1);
        }
        else 
        {
            int? visits = HttpContext.Session.GetInt32("Visit");
            int temp = Convert.ToInt32(visits);
            temp++;
            HttpContext.Session.SetInt32("Visit", temp);
        }
        string[] values = {"0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
        string password = "";
        Random rand = new Random();
        int i = 0;
        while(i < 14){
            int temp = rand.Next(0 ,values.Count());
            password += values[temp]; 
            i++;
        }
        return View("passwordgen", password);
    }
}