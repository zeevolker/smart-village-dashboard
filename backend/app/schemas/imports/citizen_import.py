from pydantic import BaseModel, Field


class ImportErrorDetail(BaseModel):
    """
    Detail error untuk setiap baris import.
    """

    row: int = Field(
        ...,
        ge=2,
        description="Nomor baris pada file Excel.",
    )

    reason: str = Field(
        ...,
        description="Alasan kegagalan import.",
    )


class CitizenImportSummary(BaseModel):
    """
    Ringkasan hasil proses import citizen.
    """

    total_rows: int = Field(
        default=0,
        ge=0,
    )

    imported: int = Field(
        default=0,
        ge=0,
    )

    duplicates: int = Field(
        default=0,
        ge=0,
    )

    failed: int = Field(
        default=0,
        ge=0,
    )

    errors: list[ImportErrorDetail] = Field(
        default_factory=list,
    )