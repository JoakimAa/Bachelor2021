using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace Bachelor2021.Model {
    public class Image {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        [Key]
        public Guid imageId { get; set; }
        public byte[] Data { get; set; }
        public string Suffix { get; set; }
    }
}
