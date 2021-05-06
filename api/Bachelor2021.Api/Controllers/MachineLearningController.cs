using Bachelor2021.Model;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Threading.Tasks;

namespace Bachelor2021.Api.Controllers {
    [Route("api/[controller]")]
    [ApiController]
    public class MachineLearningController : ControllerBase {

        [HttpPost]
        public async Task<ActionResult<Receipt>> PostImage([FromForm] ImageDTO img) {
            var image = new Image();
            var receipt = new Receipt();

            if (img != null) {
                image.Name = img.FileName;

                byte[] imageData = null;
                using (var binaryReader = new BinaryReader(img.Image.OpenReadStream())) {
                    imageData = binaryReader.ReadBytes((int)img.Image.Length);
                }

                image.ImageData = imageData;
                image.CreatedOn = DateTime.Now;
                image.FileType = Path.GetExtension(img.FileName);

                var uirWebAPI = "http://localhost:5000/v1/api/upload";

                var uri = new Uri(uirWebAPI);
                var httpWebRequest = (HttpWebRequest)WebRequest.Create(uri);
                httpWebRequest.ContentType = "application/json";
                httpWebRequest.Method = "POST";
                var base64String = Convert.ToBase64String(image.ImageData);

                await using (StreamWriter streamWriter = new StreamWriter(httpWebRequest.GetRequestStream())) {
                    dynamic imageJson = new JObject();
                    imageJson.content = base64String;
                    streamWriter.Write(imageJson.ToString());
                }
                var httpWebResponse = (HttpWebResponse)httpWebRequest.GetResponse();
                using var streamReader = new StreamReader(httpWebResponse.GetResponseStream());
                var webResponse = streamReader.ReadToEnd();
                receipt = JsonConvert.DeserializeObject<Receipt>(webResponse);
            }
            return receipt;
        }
    }
}
