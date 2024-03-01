import { useState } from "react";
import { AsyncPaginate } from "react-select-async-paginate";

const Search = ({onSearchChange}) => {
    const [search, setSearch] = useState(null);

    const handleOnChange = (searchData) => {
        setSearch(searchData);
        onSearchChange(searchData);
    }

    const getCities = async (inputValue) => {
        try {
            const response = await fetch(`api/cities/${inputValue}`);
            const response_1 = await response.json();
            return {
                options: response_1.data.map((city) => {
                    return {
                        value: `${city.latitude} ${city.longitude}`,
                        label: `${city.name}, ${city.countryCode}`,
                    };
                })
            };
        } catch (err) {
            return console.error(err);
        }
    }

    return (
        <AsyncPaginate
            placeholder="Search for a city"
            debounceTimeout={600}
            value={search}
            onChange={handleOnChange}
            loadOptions={getCities}
        />
    )
}

export default Search;