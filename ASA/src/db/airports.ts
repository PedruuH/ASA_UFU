import { Airport } from "../models/airport"

const airports = [
    {
        name: "Aeroporto de Uberlandia",
        code: "UDI",
        location: "Uberlandia"
    },
    {
        name: "Sao Paulo Internacional",
        code: "GRU",
        location: "São Paulo"
    },
    {
        name: "Rurópolis International Airport",
        code: "RUR",
        location: "Ruropolis"
    }

]


export function getAllAirports(): Airport[] {
    return airports
}
export function getAirportsByOrigin(): Airport[] {
    return []

}