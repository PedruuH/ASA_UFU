import { Flight } from "./flight";
import { User } from "./user";

export interface Eticket {
    code: String;
    flight: Flight;
    user: User;
}

