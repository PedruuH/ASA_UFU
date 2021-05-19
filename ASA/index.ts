import express from "express";
import * as dotenv from "dotenv";
import * as apiRoutes from "./routes/allRoutes";
import cors from "cors";
dotenv.config();

// rest of the code remains same
const app = express();
app.use(cors())
app.use(express.json());

const PORT = process.env.PORT || 5000;
app.use("/", apiRoutes.allRoutes);

app.listen(PORT, () => {
  console.log(`⚡️[server]: Ta rodando http://localhost:${PORT}`);
});
