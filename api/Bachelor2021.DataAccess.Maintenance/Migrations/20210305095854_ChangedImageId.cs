using Microsoft.EntityFrameworkCore.Migrations;

namespace Bachelor2021.DataAccess.Maintenance.Migrations
{
    public partial class ChangedImageId : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_Receipts_Images_ImageId",
                table: "Receipts");

            migrationBuilder.DropIndex(
                name: "IX_Receipts_ImageId",
                table: "Receipts");

            migrationBuilder.AlterColumn<int>(
                name: "ImageId",
                table: "Receipts",
                type: "int",
                nullable: false,
                defaultValue: 0,
                oldClrType: typeof(int),
                oldType: "int",
                oldNullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AlterColumn<int>(
                name: "ImageId",
                table: "Receipts",
                type: "int",
                nullable: true,
                oldClrType: typeof(int),
                oldType: "int");

            migrationBuilder.CreateIndex(
                name: "IX_Receipts_ImageId",
                table: "Receipts",
                column: "ImageId");

            migrationBuilder.AddForeignKey(
                name: "FK_Receipts_Images_ImageId",
                table: "Receipts",
                column: "ImageId",
                principalTable: "Images",
                principalColumn: "ImageId",
                onDelete: ReferentialAction.Restrict);
        }
    }
}
